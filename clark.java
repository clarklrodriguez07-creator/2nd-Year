import java.util.*;
class clark{
    public static Scanner in=new Scanner(System.in);
    public static void main(String args[]){
        int choice=0;

        do{
            System.out.println("Menu:");
            System.out.println("1. ADD");
            System.out.println("2. Search");
            System.out.println("3. Exit");
            System.out.print("Choice: ");
            choice = in.nextInt();

            switch(choice){
                case 1:
                        add();
                break;
                case 2:
                        search();
                case 3:
                    System.out.println("Exiting the program.");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }while(choice!=3);
    }

  static void add(){
        int num;
        for(int i=0;i<5;i++){
            System.out.print("Enter a number: ");
            num=clark.in.nextInt();
            if(num%2==0){
                System.out.println("Number "+ num+" is Even");
            }
                else{
                    System.out.println("Number "+ num+" is Odd");
                    }   
                }
            }

    static void search(){
        int num2;

        System.out.print("Enter a number: ");
        num2=clark.in.nextInt();
        for(int i=0;i<5;i++){
            if(num2==i){
                System.out.println("Number is found.");
            }else{
                System.out.println("Number is not found.");
                    }   
                }
            }        
}