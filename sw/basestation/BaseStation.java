import java.net.Socket;
import java.net.ServerSocket;

public class BaseStation {

  public static void main(String args[]) {
   
    try {

    ServerSocket srv = new ServerSocket(1337);
    System.out.println("Waiting for connection...");
    Socket client = srv.accept();
    System.out.println("OK!");
    int data, left, right;
    int old_left = 0, old_right = 0;

    while(true) {
      data = client.getInputStream().read();
      if(data == 0x7F) {
        left  = client.getInputStream().read(); 
        right = client.getInputStream().read(); 

	if(left != old_left || right != old_right)
          System.out.println(left + " " + right);

        old_left = left;
        old_right = right;
      }
    }
 
    } catch(Exception e) {
      System.err.println("exception: " + e);
    }
  }
}
