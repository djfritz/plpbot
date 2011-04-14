/*
    Copyright 2011 Wira Mulia, David Fritz

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

package plpbotcontrol;

/**
 *
 * @author wira
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {

        if(args.length != 1 && args.length != 3 && args.length != 4) {
            System.err.println("usage: java -jar PLPBotControl [camera's IP address] [base station IP address] [port]");
            System.err.println("OR to view camera only: java -jar PLPBotControl [camera's IP address]");

            return;
        }

        Global.streamLocator = new java.net.URL("http://" + args[0] + "/axis-cgi/jpg/image.cgi");
        if(args.length >= 3) {
            Global.baseStationHost = args[1];
            Global.baseStationPort = Integer.parseInt(args[2]);

            if(args.length == 4 && args[3].equals("wira")) {
                Global.controlFrameWira = new ControlFrameWira();
                Global.controlFrameWira.setVisible(true);
            }
            else {
                Global.controlFrame = new ControlFrame();
                Global.controlFrame.setVisible(true);
            }
            
            
        }
        Global.videoFrame = new VideoFrame();
        Global.videoFrame.setVisible(true);

        } catch(Exception e) {
            System.err.println("main exception: " + e);
        }
    }

}
