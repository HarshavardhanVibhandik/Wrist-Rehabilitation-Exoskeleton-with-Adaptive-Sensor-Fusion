**Wrist Rehabilitation Exoskeleton with Adaptive Sensor Fusion**

# **Project Objective:**
Designed a wearable robotic exoskeleton to support wrist motor recovery in post-stroke patients. The device delivers intelligent assist-as-needed therapy using real-time sensor feedback from force/torque sensors, EMG, and optical encoders. It aims to bridge the gap between clinical precision and home-based rehabilitation, enabling customizable, ergonomic recovery.

# **Project Overview:**
The exoskeleton integrates a curved rack-and-pinion mechanism for enhanced torque transmission and ROM beyond physiological limits, paired with a lightweight modular frame. Its embedded control system—Raspberry Pi 5 with Maxon EPOS4 drivers—enables real-time actuation and biofeedback regulation. Sensor fusion between EMG, flex sensors, and encoders allows torque-adaptive actuation based on user effort. The system is engineered for comfort, safety, and extended usability in both clinical and unsupervised environments.

# **Key Contributions:**

Sensor Fusion for Adaptive Therapy: Integrated EMG, force/torque sensors, and optical encoders to personalize torque delivery based on patient fatigue and intent.

Curved Rack-and-Pinion Design: Enabled a ROM of ±175° (FE), ±190° (PS), and ±90° (RU), exceeding standard therapeutic ranges while reducing friction and inertia.

Real-Time Feedback Control: Developed a Python-based interface for EPOS4 drivers using current and position control modes to apply assist-as-needed strategies dynamically.

Modular Ergonomics: Designed ambidextrous, user-adjustable supports with flexible ABS components and internal cable routing for seamless wearability.

# **Methodology:**

1. **Mechanical Architecture:**

Replaced traditional cable-based actuation with curved rack-pinion mechanisms to reduce wear and enhance precision.

Balanced the center of mass using custom rotating supports to minimize load on the pronation/supination joint.

2. **Sensor System Integration:**

Embedded EMG sensors on the forearm, flex sensors in the glove, and encoders on joint axes.

Processed multi-modal signals in real-time to adjust motor output and motion profiles dynamically.

3. **Control System:**

Employed Raspberry Pi 5 as the central controller interfacing with three Maxon EPOS4 motor drivers.

Developed modular Python scripts using the EPOS .DLL API for motion control and safety management.

4. **Fabrication and Testing:**

Fabricated load-bearing components with 70–100% infill ABS using FDM 3D printing.

Conducted multi-joint torque, ROM, and user comfort testing with healthy volunteers.

# **Challenges and Solutions:**

Sensor Noise & Calibration: Mitigated interference using shielded wiring and baseline calibration routines.

Power Management: Switched from battery to AC-adapter for extended testing sessions without performance loss.

Mechanical Resistance: Improved joint smoothness by redistributing the center of mass and minimizing structural backlash.

# **Key Outcomes:**

Achieved enhanced ROM beyond human baseline: ±175° FE, ±190° PS, and ±90° RU.

Delivered up to 1.8 Nm of torque with <5° motion deviation across joints.

High user comfort: 4.8/5 rating in fit, 4.7/5 for ease of use during trials.

Robust real-time sensor fusion enabled dynamic adjustment to individual user effort levels.

# **Technologies and Tools:**

Control & Computing: Raspberry Pi 5, Maxon EPOS4 motor drivers

Sensing: EMG sensors, Flex sensors, Force/Torque sensors, Optical encoders

Actuation: Maxon brushed DC motors, Curved rack-pinion mechanisms

Materials & CAD: ABS, Fusion 360, SolidWorks, FEA (SolidWorks Simulation)

Programming: Python, EPOS command library (EposCmd64.dll)

# **Future Improvements:**

Integrate machine learning-based adaptive impedance for smarter response under varying fatigue states.

Replace wired interfaces with Bluetooth or Wi-Fi for untethered home use.

Expand trials with ≥30 clinical patients and pursue FDA/CE certification for commercialization.

