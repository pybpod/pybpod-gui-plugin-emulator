from pybpod_gui_plugin_emulator.models.setup.setup_window_emulator import SetupWindowEmulator


class SetupUIBusyEmulator(SetupWindowEmulator):

    def update_ui(self):
        super(SetupUIBusyEmulator, self).update_ui()

        # update button on self._emulator_gui
        if hasattr(self, 'emulator_plugin'):
            if self.status == self.STATUS_READY:
                self.emulator_plugin._run_task_btn.checked = False
                self.emulator_plugin._run_task_btn.label = 'Run protocol'

            elif self.status == self.STATUS_BOARD_LOCKED:
                print("board locked")
            elif self.status == self.STATUS_RUNNING_TASK:
                self.emulator_plugin._run_task_btn.checked = True
                self.emulator_plugin._run_task_btn.label = 'Stop'

