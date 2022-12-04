import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        File file = new File("AoC1.txt");
        String text = Files.readString(Path.of("AoC1.txt"));
        BufferedReader bufReader = new BufferedReader(new StringReader(text));
        String line=null;
        List<Integer> elves = new ArrayList<>();
        int[] topThree = new int[3];
        int count = 0;
        while( (line=bufReader.readLine()) != null )
        {
            System.out.println(line);

            if(line.equals("")) {
                if(count >= topThree[0]) {
                    topThree[2] = topThree[1];
                    topThree[1] = topThree[0];
                    topThree[0] = count;
                }
                elves.add(count);
                count = 0;
                elves.add(count);
                int[] currTopThree = topThree.clone();
            }
            else {
                int lineVal = Integer.valueOf(line);
                count += lineVal;
            }
        }
        elves.stream().sorted().forEach(System.out::println);

        System.out.println(67760 + 68706 + 70116);
    }
}
