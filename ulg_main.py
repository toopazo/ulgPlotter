#!/usr/bin/env python

from tpylib_pkg.fileFolderUtils import FileFolderUtils
# from tpylib_pkg.statistics import TimeseriesStats
from ulg_parser import UlgParser
from ulg_plot_basics import UlgPlotBasics
from ulg_plot_sysid import UlgPlotSysid
from ulg_plot_mixer import UlgPlotMixer

import argparse
# import sys
# import subprocess
# import csv
# import matplotlib.pyplot as plt


class UlgMain:
    def __init__(self, logdir, tmpdir, plotdir):
        self.logdir = logdir
        self.tmpdir = tmpdir
        self.plotdir = plotdir

        self.ulg_plot_basics = UlgPlotBasics(
            self.logdir, self.tmpdir, self.plotdir)

        self.ulg_plot_sysid = UlgPlotSysid(
            self.logdir, self.tmpdir, self.plotdir)

        self.ulg_plot_mixer = UlgPlotMixer(
            self.logdir, self.tmpdir, self.plotdir)

        # Remove all files from tmpdir
        # self.ulgparser.clear_tmpdir()

    def check_ulog2csv(self, ulgfile):

        # Check if we need to run ulog2csv
        csvname = 'actuator_controls_0_0'
        csvfile = UlgParser.get_csvfile(self.tmpdir, ulgfile, csvname)
        if FileFolderUtils.is_file(csvfile):
            # UlgParser.ulog2info(ulgfile)
            pass
        else:
            UlgParser.ulog2csv(ulgfile, self.tmpdir)
            UlgParser.write_vehicle_attitude_0_deg(ulgfile, self.tmpdir)

    def process_file(self, ulgfile):

        print('[process_file] processing %s' % ulgfile)

        self.check_ulog2csv(ulgfile)

        closefig = True

        # self.ulg_plot_basics.actuator_controls_0_0(ulgfile, closefig)
        # self.ulg_plot_basics.actuator_outputs_0(ulgfile, closefig)
        # self.ulg_plot_basics.vehicle_local_position_0(ulgfile, closefig)
        # self.ulg_plot_basics.manual_control_setpoint_0(ulgfile, closefig)
        # self.ulg_plot_basics.vehicle_rates_setpoint_0(ulgfile, closefig)
        # self.ulg_plot_basics.vehicle_attitude_0_deg(ulgfile, closefig)
        # self.ulg_plot_basics.nwindow_hover_pos(ulgfile, closefig)
        # self.ulg_plot_basics.nwindow_hover_vel(ulgfile, closefig)
        #
        # self.ulg_plot_sysid.cmd_roll_to_attitude(ulgfile, closefig)
        # self.ulg_plot_sysid.cmd_pitch_to_attitude(ulgfile, closefig)
        # self.ulg_plot_sysid.cmd_yawrate_to_attitude(ulgfile, closefig)
        # self.ulg_plot_sysid.cmd_az_to_attitude(ulgfile, closefig)

        self.ulg_plot_mixer.mixer_input_output(ulgfile, closefig)
        self.ulg_plot_mixer.actuator_controls_0_0(ulgfile, closefig)
        self.ulg_plot_mixer.actuator_outputs_0(ulgfile, closefig)
        # exit(0)

        # plt.show()
        # plt.close()

    def process_logdir(self):
        print('[process_logdir] processing %s' % self.logdir)

        # foldername, extension, method
        FileFolderUtils.run_method_on_folder(ulogdir, '.ulg',
                                             ulgprocess.process_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Parse, process and plot .ulg files')
    parser.add_argument('--bdir', action='store', required=True,
                        help='Base directory of [logs, tmp, plots] folders ')
    # parser.add_argument('--plot', action='store_true', required=False,
    #                     help='plot results')
    # parser.add_argument('--loc', action='store_true', help='location')
    args = parser.parse_args()

    bdir = FileFolderUtils.full_path(args.bdir)
    # uplot = args.plot

    ulogdir = bdir + '/logs'
    utmpdir = bdir + '/tmp'
    uplotdir = bdir + '/plots'

    ulgprocess = UlgMain(ulogdir, utmpdir, uplotdir)
    ulgprocess.process_logdir()

    # 1) Go to folder
    # /home/tzo4/Dropbox/tomas/pennState/avia/software/ulgPlotter
    # 2) Activate venv
    # source venv/bin/activate
    # 3) Execute the script
    # python ulg_main.py --bdir </absolute/path>

    # Copy past this command to run the code
    # python /home/tzo4/Dropbox/tomas/pennState/avia/software/ulgPlotter/
    # ulg_main.py --bdir .

    # Or even better, run it as a package
    # python -m tpylib_pkg.ulg_main --bdir .
