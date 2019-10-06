import java.util.*;
import java.io.*;
import java.math.*;

class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt(); // the X position of the light of power
        int lightY = in.nextInt(); // the Y position of the light of power
        int initialTX = in.nextInt(); // Thor's starting X position
        int initialTY = in.nextInt(); // Thor's starting Y position
        int xDif = 0;
        int yDif = 0;
        int thorY = initialTY;
        int thorX = initialTX;
        boolean limitY = false;
        boolean limitX = false;
        String direction = "";
        // game loop
        while (true) {
            int remainingTurns = in.nextInt(); // The remaining amount of turns Thor can move. Do not remove this line.
            xDif = thorX - lightX;
            yDif = thorY - lightY;
            limitY = false;
            limitX = false;
            
            if (thorY == 17) {
                limitY = true;
            }
            
            if (thorX == 39) {
                limitX = true;   
            }
            
            if (yDif > 0 && xDif > 0) {
                direction = "NW";
                thorX--;
                thorY--;
            }
            else if (yDif > 0 && xDif == 0) {
                direction = "N";
                thorY--;
            }
            else if (yDif > 0 && xDif < 0) {
                direction = "NE";
                thorY--;
                thorX++;
            }
            else if (yDif == 0 && xDif < 0) {
                direction = "E";
            }
            else if (yDif < 0 && xDif < 0) {
                direction = "SE";
                thorX++;
                thorY++;
            }
            else if (yDif < 0 && xDif == 0) {
                direction = "S";
                thorY++;
            }
            else if (yDif < 0 && xDif > 0) {
                direction = "SW";
                thorX--;
                thorY++;
            }
            else if (yDif == 0 && xDif > 0) {
                direction = "W";
                thorX--;
            }
            
            if (limitY == true) {
                switch (direction) {
                    case "SE": direction = "E"; break;
                    case "SW": direction = "W"; break;
                }
            }
            else if (limitX == true) {
                switch (direction) {
                    case "NW": direction = "W"; break;
                    case "NE": direction = "E"; break;
                }
            }
            
            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");
            System.err.println(limitY);

            // A single line providing the move to be made: N NE E SE S SW W or NW
            System.out.println(direction);
        }
    }
}