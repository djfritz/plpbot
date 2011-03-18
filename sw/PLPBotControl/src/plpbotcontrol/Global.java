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
import java.awt.Image;

/**
 *
 * @author wira
 */
public class Global {
    public static VideoFrame    videoFrame;
    public static URL           streamLocator;
    public static URLConnection streamConnection;
    public static Image         streamFrame;

    public static int           buffers = 10;
}
