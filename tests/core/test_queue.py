"""Tests for queue hook failure handling."""

from unittest.mock import patch

from shelfmark.core.models import DownloadTask, QueueStatus
from shelfmark.core.queue import BookQueue


def _make_task(task_id: str = "task-1") -> DownloadTask:
    return DownloadTask(
        task_id=task_id,
        source="direct_download",
        title="Example Title",
        user_id=1,
        username="alice",
    )


def test_add_logs_queue_hook_failures():
    queue = BookQueue()

    def broken_hook(task_id: str, task: DownloadTask) -> None:
        raise RuntimeError("boom")

    queue.set_queue_hook(broken_hook)

    with patch("shelfmark.core.queue.logger.warning") as mock_warning:
        assert queue.add(_make_task()) is True

    mock_warning.assert_called_once()
    args = mock_warning.call_args.args
    assert args[0] == "Queue hook failed while adding task %s: %s"
    assert args[1] == "task-1"
    assert str(args[2]) == "boom"


def test_enqueue_existing_logs_queue_hook_failures():
    queue = BookQueue()
    assert queue.add(_make_task("task-2")) is True

    def broken_hook(task_id: str, task: DownloadTask) -> None:
        raise RuntimeError("boom")

    queue.set_queue_hook(broken_hook)

    with patch("shelfmark.core.queue.logger.warning") as mock_warning:
        assert queue.enqueue_existing("task-2") is True

    mock_warning.assert_called_once()
    args = mock_warning.call_args.args
    assert args[0] == "Queue hook failed while requeueing task %s: %s"
    assert args[1] == "task-2"
    assert str(args[2]) == "boom"


def test_add_refuses_completed_task_without_force():
    queue = BookQueue()
    task = _make_task("done-1")
    assert queue.add(task) is True
    queue.update_status("done-1", QueueStatus.COMPLETE)

    assert queue.add(_make_task("done-1")) is False
    assert queue.get_task_status("done-1") == QueueStatus.COMPLETE


def test_add_force_requeues_completed_task():
    queue = BookQueue()
    first = _make_task("done-2")
    first.staged_path = "/tmp/old.epub"
    first.progress = 1.0
    assert queue.add(first) is True
    queue.update_status("done-2", QueueStatus.COMPLETE)

    replacement = _make_task("done-2")
    replacement.title = "Requeued Title"
    assert queue.add(replacement, force=True) is True
    assert queue.get_task_status("done-2") == QueueStatus.QUEUED
    stored = queue.get_task("done-2")
    assert stored is replacement
    assert stored.title == "Requeued Title"
    assert first.staged_path == "/tmp/old.epub"
    assert first.progress == 1.0


def test_add_force_refuses_downloading_task():
    queue = BookQueue()
    assert queue.add(_make_task("live-1")) is True
    queue.update_status("live-1", QueueStatus.DOWNLOADING)

    assert queue.add(_make_task("live-1"), force=True) is False
    assert queue.get_task_status("live-1") == QueueStatus.DOWNLOADING


def test_add_force_refuses_queued_task():
    queue = BookQueue()
    assert queue.add(_make_task("queued-1")) is True

    assert queue.add(_make_task("queued-1"), force=True) is False
    assert queue.get_task_status("queued-1") == QueueStatus.QUEUED
