import clr
import ctypes
import time
import sys
import os
import ctypes
clr.AddReference('EposCmd.Net')
#EposCmd64 = ctypes.CDLL('.\EposCmd64.dll')
from EposCmd.Net.VcsWrapper import Device
import re
from System import IntPtr


# Create variables to hold the output parameters
inverted_polarity = ctypes.c_bool(False)
resolution = ctypes.c_ulong(0)
inverted_param = ctypes.c_bool(True)
error_code = ctypes.c_ulong(0)
#num = ctypes.c_ulong(1)
#den = ctypes.c_ulong(1)
nodeid = ctypes.c_ushort(1)
#resoultion = ctypes.c_ulong(360)


# parameters
errorCode = 0
nodeID = 1
baudrate = 1000000
timeout = 500
absolute = False #as opposed to relative
immediately = True #does not wait for execution of previous command
pos0 = 0
delta_angle = 0 # record the change of angle
num = 1
den = 1

dll_path = r'C:\Users\tatin\OneDrive\Desktop\exo\MaxonMotor-control-with-EPOS4\EposCmd64.dll' #path for EposCmd4.dll

# Add the DLL directory to the system PATH
os.environ['PATH'] = os.path.dirname(dll_path) + ';' + os.environ['PATH']

# Load the DLL
try:
    EposCmd64 = ctypes.CDLL(dll_path)
except OSError as e:
    print(f"Failed to load DLL: {e}")
    print("Check dependencies with Dependency Walker")

class Motor:
    def _init_(self, angle, direction, velocity, acceleration, deceleration, pos, actualPos, actualVel, encvalue, encvalue1):
        self.angle = angle
        self.direction = direction
        self.velocity = velocity
        self.acceleration = acceleration
        self.deceleration = deceleration
        self.pos = pos
        self.actualPos = actualPos
        self.actualVel = actualVel
        self.encvalue = encvalue
        self.encvalue1 = encvalue1
        
def connection():
    errorCode = 0
    Device.Init()
    keyHandle, error = Device.VcsOpenDevice('EPOS4', 'MAXON SERIAL V2', 'USB', 'USB0', errorCode) #opens EPOS
    if keyHandle == 0:
        print("Please turn on Power Supply!\n")
    return keyHandle

def initial(name):
    name.angle = 0
    name.direction = 0
    name.encvalue = 0
    name.velocity = 5000 #rpm profile speed
    name.acceleration = 100000 #rpm/s, up to 1e7 would be possible
    name.deceleration = 100000 #rpm/s
    name.pos = 1000000000
    name.pos = 350
    name.actualpos = 0
    name.encvalue1 = 0
    return name

# start
def settings(keyHandle, name):
    # Set protocol and clear faults
    Device.VcsSetProtocolStackSettings(keyHandle, baudrate, timeout, errorCode)
    Device.VcsClearFault(keyHandle, nodeID, errorCode)

    
    EposCmd64.VCS_SetSensorType(keyHandle, nodeID, 2, ctypes.byref(error_code))
    Device.VcsActivateMasterEncoderMode(keyHandle, nodeID, errorCode)
    EposCmd64.VCS_SetIncEncoderParameter(keyHandle, nodeID, ctypes.byref(resolution), ctypes.byref(inverted_polarity), ctypes.byref(error_code))
    Device.VcsSetMasterEncoderParameter(keyHandle, nodeID, num, den, 0, name.velocity, name.acceleration, errorCode)
    #print(error_code)
    
    # Activate Profile Position Mode and set parameters
    Device.VcsActivateProfilePositionMode(keyHandle, nodeID, errorCode)
    Device.VcsSetPositionProfile(keyHandle, nodeID, name.velocity, name.acceleration, name.deceleration, errorCode)
    
    # Enable the device
    Device.VcsSetEnableState(keyHandle, nodeID, errorCode)

def start(name):
    
    resolution = ctypes.c_ulong(2048)
    # angle limit
    
    keyHandle = connection()
    name.actualPos = (Device.VcsGetPositionIs(keyHandle, nodeID, name.pos, errorCode))[1]
    name.actualVel = (Device.VcsGetVelocityIs(keyHandle, nodeID, name.velocity, errorCode))[1]
    settings(keyHandle, name)
        
    a = 60
    delay = a/6/name.velocity
                
        # delta angle calculation
    if name.angle > 0:
        name.direction = 1
    elif name.angle < 0:
        name.direction = -1
    else:
        name.direction = 0
       
        #ANGLE, name.direction, delta_angle = DELTA_ANGLE(ANGLE, name.direction, delta_angle)
                
        # continue
    timewait = 40 * abs(name.angle)
    pos1 =  10 * name.direction * name.angle  #10 as scaling value

    name.actualPos = (Device.VcsGetPositionIs(keyHandle, nodeID, pos1, errorCode))[1]
    name.actualVel = (Device.VcsGetVelocityIs(keyHandle, nodeID, name.velocity, errorCode))[1]
        
    Device.VcsSetEnableState(keyHandle, nodeID, errorCode) #enable device 
                
    Device.VcsMoveToPosition(keyHandle, nodeID, pos1, absolute, immediately, errorCode)
     time.sleep(delay)
    Device.VcsWaitForTargetReached(keyHandle, nodeID, timewait, errorCode)
    name.actualPos = (Device.VcsGetPositionIs(keyHandle, nodeID, pos1, errorCode))[1]

    name.encvalue = (Device.VcsGetMasterEncoderParameter(keyHandle, nodeID, num, den, 1, name.velocity, name.acceleration, errorCode))
    # Call the function with proper pointers
    # print(resolution,type(resolution),resolution.value)
    encoder_value = EposCmd64.VCS_GetIncEncoderParameter(keyHandle, nodeid, ctypes.byref(resolution), ctypes.byref(inverted_polarity), ctypes.byref(error_code))
    #print(type(resolution))
    name.encvalue1 = resolution.value
    print(resolution.value)

    Device.VcsSetDisableState(keyHandle, nodeID, errorCode)
        
