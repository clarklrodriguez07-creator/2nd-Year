import java.util.*;
class clark{
    public static Scanner in=new Scanner(System.in);
    public static int num[]=new int[5];
    public static void main(String args[]){
        int choice=0;

        do{
            System.out.println("Menu:");
            System.out.println("1. ADD");
            System.out.println("2. Search");
            System.out.println("3. Modify");
            System.out.println("4. Show All");
            System.out.println("5. Exit");
            System.out.print("Choice: ");
            choice = in.nextInt();

            switch(choice){
                case 1:
                        add();
                        break;
                case 2:
                        search();
                        break;
                case 3:
                        Modify();
                        break;
                case 4:
                        ShowAll();
                        break;
                case 5:
                    System.out.println("Exiting the program.");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }while(choice!=4);
    }

  static void add(){
        for(int i=0;i<5;i++){
            System.out.print("Enter a number: ");
            num[i]=clark.in.nextInt();
            if(num[i]%2==0){
                System.out.println("Number "+ num[i]+" is Even");
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
            if(num2==num[i]){
                System.out.println("Number "+ num2 +" is found.");
                return;
            }else{
                System.out.println("Number "+ num2 +" is not found.");
            }
        }
    }       
    
    static void Modify(){
        int num2;

        System.out.print("Enter a number to modify: ");
        num2=clark.in.nextInt();
        for(int i=0;i<5;i++){
            if(num2==num[i]){
                System.out.print("Enter the new number: ");
                num[i]=clark.in.nextInt();
                System.out.println("Number "+ num2 +" has been modified.");
                return;
            }
        }
        System.out.println("Number "+ num2 +" is not found.");
    }             

    static void ShowAll(){
        for(int i=0;i<5;i++){
            System.out.println("Number "+ (i+1) +": "+ num[i]);
        }
    }
} 
