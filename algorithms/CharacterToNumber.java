package algorithms;

public class CharacterToNumber {
    

    public static int parseInt(String text){
        
        int number = 0;
        int powerIncreament =  0;

        for (int i = text.length()- 1; i >=0; i--){
            char c = text.charAt(i);
            number += Math.pow(26, powerIncreament)* ((int)c - (int)'A' + 1);
            powerIncreament++;
        }
        return number;
    }
        
public static void main(String[] args) {

    System.out.println(CharacterToNumber.parseInt("A"));
}

}
