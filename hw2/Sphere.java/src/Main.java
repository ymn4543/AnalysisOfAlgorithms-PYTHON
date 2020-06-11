import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int numpoints = Integer.parseInt(in.nextLine());
        int distances[];
        for(int x = 0; x<numpoints;x++){
            String point = in.nextLine();
            System.out.print(point +  "\n");
        }

    }
}
