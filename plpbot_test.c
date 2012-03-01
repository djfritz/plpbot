int get_uart(void) {
	void *uart  = 0xf0000000;
	void *status = 0xf0000004;
	void *rec = 0xf0000008;
	while (*status == 1);
	*uart = 2;
	return *rec;
}

int set_motor(int a) {
	void *uart  = 0xf0c00000;
	void *status = 0xf0c00004;
	void *send = 0xf0c0000c;
	while (*status == 0);
	*send = a;
	*uart = 1;
	return 0;
}


void main(void) {
        int input;
	void *leds = 0xf0200000;

        while (1) {
		input = get_uart(0);
		*leds = input;
		set_motor(input);
        }
}
