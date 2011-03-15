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

        Global.streamLocator = new java.net.URI(args[0]);
        (new VideoFrame()).setVisible(true);

        } catch(Exception e) {
            System.err.println("dumbass: " + e);
        }
    }

}
