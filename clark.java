import java.util.*;
class clark{
    public static Scanner in=new Scanner(System.in);
    public static void main(String args[]){
        int num;

        for(int i=0;i<5;i++){
            System.out.print("Enter a number: ");
            num=in.nextInt();
            if(num%2==0){
                System.out.println("Number "+ num+" is Even");
            }
            else{
                System.out.println("Number "+ num+" is Odd");
            }
        }
    }

}