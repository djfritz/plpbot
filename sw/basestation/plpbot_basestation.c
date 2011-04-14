/* 

fritz
3.24.2010

simple basestation relay for the plpbot

usage: ./plpbot_basestation <serial port>

The software listens on the official plpbot server port, 1337.

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>
#include <sys/time.h>

#include <sys/stat.h>
#include <fcntl.h>
#include <termios.h>

struct plpbot_packet {
	unsigned char startbyte;
	unsigned char left_motor;
	unsigned char right_motor;
};

#define PORT 1337

static suseconds_t old_time;

void handle_packet(struct plpbot_packet p, int serialfd) {
	if (p.startbyte != 0x7f) {
		printf("[w] invalid packet\n");
	} else {
		/* write the motor values */
		write(serialfd, &p, sizeof(struct plpbot_packet));
	}
}

int main(int argc, char *argv[]) {
	int sockfd, newsockfd;
	socklen_t clilen;
	struct sockaddr_in serv_addr, cli_addr;

	int serialfd,c,res;
	struct termios oldtio, newtio;

	if (argc != 2) {
		printf("usage: ./bs <serial device>\n");
		exit(-1);
	}

	printf("[i] plpbot base station\n");

	printf("[i] opening serial device\n");
	serialfd = open(argv[1], O_RDWR | O_NOCTTY);
	if (serialfd < 0) {
		printf("[e] opening serial device\n");	
		exit(-1);
	}	

	tcgetattr(serialfd, &oldtio);
	memset(&newtio, 0, sizeof(struct termios));

	newtio.c_cflag = B57600 | CRTSCTS | CS8 | CLOCAL | CREAD;
	newtio.c_iflag = IGNPAR | ICRNL;
	newtio.c_oflag = 0;
	newtio.c_lflag = ICANON;

	tcflush(serialfd, TCIFLUSH);
	tcsetattr(serialfd, TCSANOW, &newtio);

	printf("[i] opening socket\n");
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd < 0) {
		printf("[e] opening socket\n");
		exit(-1);
	}

	memset(&serv_addr, 0, sizeof(serv_addr));
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = INADDR_ANY;
	serv_addr.sin_port = htons(PORT);
	if (bind(sockfd, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) < 0) {
		printf("[e] bind\n");
		exit(-1);
	}

	listen(sockfd,1);
	clilen = sizeof(struct sockaddr_in);
	while (1) {
		struct plpbot_packet p;
		ssize_t size;

		printf("[i] listening for clients\n");

		/* grab a connection */
		newsockfd = accept(sockfd, (struct sockaddr*) &cli_addr, &clilen);
		if (newsockfd < 0) {
			printf("[e] accept\n");
			exit(-1);
		}
		printf("[i] client connected\n");

		/* grab data */
		while (size = recv(newsockfd, &p, sizeof(struct plpbot_packet), MSG_WAITALL) == sizeof(struct plpbot_packet)) {
			
			struct timeval tv;
			gettimeofday(&tv,NULL);

			printf("[i] %x, %d, %d, %d ms\n", p.startbyte, p.left_motor, p.right_motor, (tv.tv_usec - old_time)/1000);
			
			old_time = tv.tv_usec;			

			handle_packet(p,serialfd);
		}

		/* if we're here we lost a connection */
		printf("[w] dropped connection!\n");
		
		close(newsockfd);
	}

	return 0;
}

