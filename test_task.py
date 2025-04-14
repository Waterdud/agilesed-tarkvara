from task import task

def test_mark_don():
    task = Task("Testi ülesanne")
    task.mark_done()
    assert task.status =="done"