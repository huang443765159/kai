from PyQt5.QtCore import QObject, QTimer
from QTimer任务流模块.JobModel import OneJob


class TaskFlow(QObject):

    def __init__(self):
        super().__init__()
        # FLOW
        self._task_flow = dict()
        self._timer = QTimer()
        self._timer.setSingleShot(True)  # 让self._timer只执行一遍。  QTimer().signalShot(500, fun)是执行一次的函数
        self._fun_start = None
        self._fun_stop = None

    def __setitem__(self, key, value):
        self._task_flow[key] = value

    def __getitem__(self, key):
        return self._task_flow[key]

    def get_flow(self):
        for value in self._task_flow.values():
            fun_start, fun_stop, timer, fun_type = value
            if timer:
                if fun_stop == 'Start':
                    self._timer.start(timer)
                    self._timer.timeout.connect(fun_start)
                else:
                    # self._fun_start, self._fun_stop = fun_start, fun_stop
                    self._timer.start(timer)
                    self._timer.timeout.connect(self.finished)
                    fun_stop.connect(fun_start)

    def finished(self):
        pass
        # self._fun_stop.connect(self._fun_start)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    _jobs = ['Task1', 'Task2', 'Task3']
    _time_outs = [500, 500, 500]
    # JOBS
    jobs = dict()
    for _sid, _job in enumerate(_jobs):
        jobs[_sid] = OneJob(timeout=_time_outs[_sid], job_name=_job)

    _task = TaskFlow()
    _task[0] = [jobs[0].start, 'Start', 1000, None]
    _task[1] = [jobs[1].start, jobs[0].sign_finished, 5000, True]
    _task[2] = [jobs[2].start, jobs[1].sign_finished, 1000, True]
    _task.get_flow()
    # jobs[1].sign_finished.connect(print)

    sys.exit(app.exec_())
