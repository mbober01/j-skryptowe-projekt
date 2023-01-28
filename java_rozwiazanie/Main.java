import java.util.ArrayList;

public class Main {

    public static String algorithm(String seq) {
        ArrayList<Character> list = new ArrayList<>();
        for (Character c : seq.toCharArray()) {
            list.add(c);
        }
        int length = list.size();
        int temp = 0;
        for (int x = 0; x < length; x++) {
            temp = 0;
            for (int index = x+1; index < (length+x)/2+1; index++) {
                temp += 1;
                ArrayList<Character> part1 = new ArrayList<>(list.subList(x, index));
                ArrayList<Character> part2 = new ArrayList<>(list.subList(index, index+temp));
                if (part1.equals(part2)) {
                    return "nie jest niepowtarzalny " + part1;
                }
            }
        }
        return "jest niepowtarzalny";
    }

    public static void main(String[] args) {

        String[] inputs = {"123231", "2343324", "123213", "324321"};
        for(String input:inputs){
            System.out.printf("input: %s\noutput: %s\n",input,algorithm(input));
            System.out.println("---------------------------------");
        }
    }
}