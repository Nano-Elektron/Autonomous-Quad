byte PWM_PIN1 = 3;
byte PWM_PIN2 = 5;
byte PWM_PIN3 = 6;
byte PWM_PIN4 = 9;
byte PWM_PIN5 = 10;

int pwm_value1;
int pwm_value2;
int pwm_value3;
int pwm_value4;
int pwm_value5;
 
void setup() {
  pinMode(PWM_PIN1, INPUT);
  pinMode(PWM_PIN2, INPUT);
  pinMode(PWM_PIN3, INPUT);
  pinMode(PWM_PIN4, INPUT);
  pinMode(PWM_PIN5, INPUT);
 
  Serial.begin(115200);
}
 
void loop() {
  pwm_value1 = pulseIn(PWM_PIN1, HIGH);
  pwm_value2 = pulseIn(PWM_PIN2, HIGH);
  pwm_value3 = pulseIn(PWM_PIN3, HIGH);
  pwm_value4 = pulseIn(PWM_PIN4, HIGH);

  
  Serial.print((float)pwm_value1/200);
  Serial.print(' ');
  Serial.print((float)pwm_value2/200);
  Serial.print(' ');
  Serial.print((float)pwm_value3/200);
  Serial.print(' ');
  Serial.print((float)pwm_value4/200);


  Serial.println();
}