import RPi.GPIO as IO
import time

class ramp_pwm_bidirectional():

    def __init__(self, GPIO_header_num, low_pwm_percent, high_pwm_percent, pwm_frequency, ramp_interval):
        self.low_pwm_percent =  low_pwm_percent
        self.high_pwm_percent = high_pwm_percent
        self.GPIO_header_num = GPIO_header_num
        self.pwm_frequency = pwm_frequency
        self.ramp_interval = ramp_interval        
        self.pwm_module_object = IO.PWM(self.GPIO_header_num, pwm_frequency)
    
    def ramp_up(self):
        self.pwm_module_object.start(0)       
        [self.ramp_interval_function(x) for x in range(self.low_pwm_percent, high_pwm_percent)]        
        time.sleep(4)
        
    def ramp_down(self, curr_pwm_percent):
        #currently running at curr_pwm_percent using PWM
        [self.ramp_interval_function(x) for x in range(curr_pwm_percent, self.high_pwm_percent, -1) ]        
        
    def ramp_interval_function(self, interim_pwm_percent):
        self.pwm_module_object.ChangeDutyCycle(interim_pwm_percent)
        time.sleep(self.ramp_interval)

if __name__ == '__main__':
    #static variables for ramping
    GPIO_pin_num = 19
    low_pwm_percent = 10
    high_pwm_percent = 50
    pwm_frequency = 2000
    ramp_interval = 0.5

    
    #IO.setwarnings(False)  
    IO.setmode(IO.BCM)
    IO.setup(GPIO_pin_num, IO.OUT)
    
    running = ramp_pwm_bidirectional(GPIO_pin_num, low_pwm_percent, high_pwm_percent, pwm_frequency, ramp_interval )
