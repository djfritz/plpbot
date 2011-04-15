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

import java.net.URL;
import java.net.URLConnection;
import java.net.Socket;
import java.awt.Image;

/**
 *
 * @author wira
 */
public class Global {
    public static VideoFrame    videoFrame;
    public static ControlFrame  controlFrame;
    public static ControlFrameWira  controlFrameWira;
    public static Socket        baseStation;
    public static String        streamLocator;
    public static URLConnection streamConnection;
    public static Image         streamFrame;
    public static String        baseStationHost;
    public static int           baseStationPort;

    public static int           buffers = 10;

    public static int           grabberRate = 0;
    public static int           painterRate = 0;
    public static int           senderRate = 50;

    public static int           comboKeyOffset = 30;
    public static int           turnOffsetIncrement = 10;
}
