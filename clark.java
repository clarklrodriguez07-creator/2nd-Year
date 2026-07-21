import java.util.*;
class clark{
    public static Scanner in=new Scanner(System.in);
    public static void main(String args[]){
        int num;
        int choice=0;

        do{
            System.out.println("Menu:");
            System.out.println("1. ADD Number");
            System.out.println("2. Exit");
            System.out.print("Choice: ");
            choice = in.nextInt();
        if(choice==1){
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
        else if(choice==2){
            System.out.println("Exiting the program.");
        }
        else{
            System.out.println("Invalid choice. Please try again.");
        }
    }while(choice!=2);
  }
}