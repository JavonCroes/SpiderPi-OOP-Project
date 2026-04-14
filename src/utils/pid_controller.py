class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        
        self.last_error = 0
        self.integral = 0

    def update(self, error):
        # P: Proportioneel (hoe ver staan we er vanaf?)
        p_term = self.kp * error
        
        # I: Integraal (staan we al lang naast het doel?)
        self.integral += error
        i_term = self.ki * self.integral
        
        # D: Afgeleide (hoe snel naderen we het doel?)
        derivative = error - self.last_error
        d_term = self.kd * derivative
        
        # De output is de som van deze drie
        output = p_term + i_term + d_term
        
        # Onthoud de error voor de volgende keer
        self.last_error = error
        
        return output