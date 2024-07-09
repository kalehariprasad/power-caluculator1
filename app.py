import streamlit as st
import math

class Power:
    def __init__(self, voltage, current):
        self.voltage = voltage
        self.current = current

    def __str__(self):
        return '{},{}'.format(self.voltage, self.current)

    def resistance(self):
     if self.current != 0:
        R = self.voltage / self.current
        return 'total resistance is {} ohms'.format(R)
     else:
        return 'Cannot divide by zero. Please provide a non-zero value for current.'


    def w(self):
        power_factor = math.cos(self.voltage * self.current)
        w = (self.voltage * self.current * power_factor )
        return "total power is {} W".format(w)

    def va(self):
        VA = (1.372 * (self.voltage * self.current))
        return "total apparent power is {} VA".format(VA)

    def power_factor(self):
        pf = math.cos(self.voltage * self.current)
        return 'power factor is {} '.format(pf)

    def kwh(self, time):
        self.time = time
        if type(time)==int:
            wh = ((self.voltage * self.current) * (time * 60))/1000
            
            
            return 'total consumption for given runtime is {} WH'.format(wh)
        else:
            return 'provide time in hours'
        
     
        
        
 
def main():
    st.title("Power Calculation App")

    # Input fields for voltage and current
    voltage = st.number_input("Enter voltage:")
    current = st.number_input("Enter current:")

    # Create an instance of the Power class
    power_obj = Power(voltage, current)

    # Calculate and display the results
    st.subheader("Results:")
    st.write("Resistance:", power_obj.resistance())
    st.write("Power (W):", power_obj.w())
    st.write("Apparent Power (VA):", power_obj.va())
    st.write("Power Factor:", power_obj.power_factor())

    # Input field for runtime
    time = st.number_input("Enter runtime (in hours):")

    # Calculate and display the energy consumption
    st.subheader("Energy Consumption:")
    st.write(power_obj.kwh(int(time)))
    
 
if __name__ == '__main__':
    main()
