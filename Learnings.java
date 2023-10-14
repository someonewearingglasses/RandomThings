public class Learnings {
    public static void main(String[] args) {

        //f-string format
        String name = "James";
        int age = 19;
        System.out.printf("I am %s, %d years old ", name, age);

        //Converting data types
        int i = 5;
        char c = 5;
        String s = 5;
            // any(specific object) to string
        String is = Integer.toString(i);
        String cs = Character.toString(c);
            // String to int
        int si = Integer.parseInt(i);
            // char to int
        int ci1 = Integer.parseInt(Character.toString(c));
        int ci2 = c - '0';
    }
}
