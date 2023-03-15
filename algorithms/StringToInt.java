package algorithms;

class StringToInt{

    public static int parseInt(String text){
        
        int number = 0;
        int powerIncreament =  0;

        for (int i = text.length()- 1; i >=0; i--){
            char c = text.charAt(i);
            number += Math.pow(10, powerIncreament)* ((int)c - (int)'0');
            powerIncreament++;
        }
        return number;
    }
        
public static void main(String[] args) {

    System.out.println(StringToInt.parseInt("12345"));
}
}
