import java.util.*;
class Main {
    public static int i=0;
    public static Scanner in=new Scanner(System.in);
    public static void main(String[] args) {
    boolean loop=true;  
    int choice=0;
    String again;
    
    Employee[] employee=new Employee[100];
       
    do{
    System.out.println();
    System.out.print("---------MENU--------");
    System.out.println("\n1. Add Employee");
    System.out.println("2. Search Employee");
    System.out.println("3. Update Employee");
    System.out.println("4. Delete Employee");
    System.out.println("5. Display All Employee");
    System.out.println("6. Exit");
    System.out.println("---------------------");
    while(true){
    System.out.print("Choose: ");
    if(in.hasNextInt()){
        choice=in.nextInt();
        break;
    }else{
    System.out.println("Invalid input. Try again.");
    in.next();
        }
    }
    System.out.println();

    switch(choice){
        case 1: 
            add(employee, in);
            break;
        case 2: 
            search(employee, in);
            break;
        case 3: 
            update(employee, in);
            break;
        case 4:
            delete(employee, in);
            break;
        case 5: 
            check();
            displayAll(employee);
            break;
        case 6: 
        System.out.println("Exiting."); 
        loop=false; 
        break;
        default: 
        System.out.println("Invalid input."); 
        break;
         }
            
  
    }while(loop);   
    System.out.println("Program Terminated");
}

static void add(Employee[] employee, Scanner in) {
    String again;

    do{
        if(i<employee.length){
        employee[i]=new Employee();
        employee[i].input(employee, i, in);
            if(employee[i].valid){
            employee[i].compute();
            employee[i].display();
            i++;
            }else{
            employee[i] = null;
            return;
            }
            }else{
            System.out.println("Employee list is full.");
            }

        while(true){
        System.out.print("\nSame Transaction? (yes, otherwise no): ");
        again = in.nextLine();
        if(again.matches("[a-zA-Z]+")){
        break;
        }else{
        System.out.println("\nInvalid input. Letters only.");
        }
    }

    }while(again.equalsIgnoreCase("yes"));
}

static void search(Employee[] employee, Scanner in) {
    String again;

    do{
        if(i==0){
        System.out.println("Empty Record/Array.");
        return;
    }

    while(true){
        int search1;
        
        while(true){
            System.out.print("Enter Employee Number to search: ");
            if(in.hasNextInt()){
                search1=in.nextInt();
                in.nextLine();
                break;
            }else{
                System.out.println("Invalid input. Try again.");
                in.next();
            }
        }

        boolean found=false;

        for(int x=0;x<i;x++){
            if(employee[x].empnumber==search1){
                found=true;
                employee[x].display();
                break;
            }
        }
        
        if(!found){
            System.out.println("Not found in the record/list. Try again.");
        }else{
            break;
        }
    }
     while(true){
        System.out.print("\nSame Transaction? (yes, otherwise no): ");
        again = in.nextLine();
        if(again.matches("[a-zA-Z ]+")){
        break;
        }else{
        System.out.println("\nInvalid input. Letters only.");
        }
    }
    }while(again.equalsIgnoreCase("yes"));
}

static void update(Employee[] employee, Scanner in){
    String again;
    do{
        while(true){
        if(i==0){
        System.out.println("Empty Record/Array.");
        return;
        }
        int search2;
        while(true){
            System.out.print("Enter Employee Number to Update: ");
            if(in.hasNextInt()){
                search2=in.nextInt();
                in.nextLine();
                break;
            }else{
                System.out.println("Invalid input. Try again.");
                in.next();
            }
        }

        boolean found=false;

        for(int x=0;x<i;x++){
            if (employee[x].empnumber==search2) {
                found=true;

                System.out.println("\nEmployee Found. Enter new details:");

                while(true){
                    System.out.print("New Hours Worked: ");
                    if(in.hasNextDouble()){
                        employee[x].hours=in.nextDouble();
                        in.nextLine();
                        break;
                    }else{
                        System.out.println("Invalid input. Try again.");
                        in.next();
                    }
                }

                while(true){
                    System.out.print("New Employment Status(regular,probationary,contractual,temporary): ");
                    String text=in.nextLine();

                    if(text.matches("[a-zA-Z ]+")){
                        employee[x].empstat=text;
                        break;
                    }else{
                        System.out.println("Invalid input. Try again.");
                    }
                }

                while(true){
                    System.out.print("New Civil Status(single,married,widowed): ");
                    String text2=in.nextLine();

                    if(text2.matches("[a-zA-Z ]+")) {
                        employee[x].civstat=text2;
                        break;
                    }else{
                        System.out.println("Invalid input. Try again.");
                    }
                }
               
                employee[x].compute();
                employee[x].display();
                
                System.out.println("\nEmployee Updated Successfully.");
                break;
            }
        }

        if(!found){
            System.out.println("Not found in the record/list.");
        }else{
            break;
        }
    }

    System.out.print("\nSame Transaction? (yes, otherwise no): ");
    again = in.next();
    in.nextLine();
    }while(again.equalsIgnoreCase("yes"));
}

static void delete(Employee[] employee, Scanner in){
    String again;

    do{
        while(true){
        if(i==0){
            System.out.println("Empty Record/Array.");
            return;
        }

        int search;

        while(true){
            System.out.print("Enter Employee Number to Delete: ");
            if(in.hasNextInt()){
                search=in.nextInt();
                in.nextLine();
                break;
            }else{
                System.out.println("Invalid input. Try again.");
                in.next();
            }
        }

        boolean found=false;

        for(int x=0;x<i;x++){
            if(employee[x].empnumber==search){
                found=true;

                System.out.println("\nEmployee Found:");

                for(int y=x;y<i-1;y++){
                    employee[y]=employee[y+1];
                }

                employee[i-1]=null;
                i--;

                System.out.println("\nEmployee Number is delete.");
                displayAll(employee);
                break;
            }
        }

        if(!found){
            System.out.println("Employee Not found in the record/list.");
        }else{
            break;
        }
    }

    System.out.print("\nSame Transaction? (yes, otherwise no): ");
    again=in.next();
    in.nextLine();
    }while(again.equalsIgnoreCase("yes"));
}
 
static void displayAll(Employee[] employee){
    String again;
  
    if(i==0){
        return;
        }
    
    System.out.println("========ALL EMPLOYEES========");
    for (int x=0;x<i;x++){
        System.out.println("Employee Number: " + employee[x].empnumber);
        System.out.println("Employee Name: " + employee[x].empName);
        System.out.println("Hours Worked: " + employee[x].hours);
        System.out.println("Employment Status: " + employee[x].empstat);
        System.out.println("Civil Status: " + employee[x].civstat);
        System.out.println("Dependent: " + employee[x].dependent);
        System.out.println("Labor Member Union: " + employee[x].labor);
        System.out.println("Company Loan Program: " + employee[x].company);
        System.out.println("Basic Pay: " + employee[x].basicpay);
        System.out.println("Overtime Pay: " + employee[x].overpay);
        System.out.println("Gross Income: " + employee[x].gross);
        System.out.println("Total Deductions: " + employee[x].totalded);
        System.out.println("Net Income: " + employee[x].netincome);
        System.out.println("--------------------------------");
    }
    System.out.println("======== END OF RECORD ========\n");
    }

static void check(){
    if(i==0){
        System.out.println("Empty Record/Array.");
        }
}

}


class Employee {
    int empnumber, dependent; 
    double hours, overtime; 
    String empName, empstat, civstat, labor, company;
    double basicpay, overpay, gross, totalded, netincome;
    boolean valid=false;
    String again;

    public void input(Employee[] employee, int size, Scanner in) {
    while(true){
    System.out.print("Employee Number: ");
    if(in.hasNextInt()){
    int num=in.nextInt();
    in.nextLine();

    boolean dupe=false;

    for(int x=0;x<size;x++) {
        if(employee[x].empnumber==num) {
            dupe=true;
            break;
        }
    }

    if(dupe){
    System.out.println("Employee is on the Record/List");

     while(true){
        System.out.print("\nSame Transaction? (yes, otherwise no): ");
        again = in.nextLine();
        if(again.matches("[a-zA-Z]+")){
        break;
        }else{
        System.out.println("\nInvalid input. Letters only.");
        }
    }

    if(again.equalsIgnoreCase("yes")){
    continue;
    }else{
    return;
    }
    }

    empnumber = num;
    break;

        }else{
        System.out.println("Invalid input. Try again.");
        in.next();
        }
    }

    while(true){
    System.out.print("Employee Name: ");
    String text=in.nextLine();
    if(text.matches("[a-zA-Z ]+")){
    empName=text;
    break;
    }else{
    System.out.println("Invalid input. Try again.");
        }
    }
    
    while(true){
    System.out.print("Hours Work: ");
    if(in.hasNextDouble()){
    hours=in.nextDouble();
    in.nextLine();
    break;
    }else{
    System.out.println("Invalid input. Try again.");
    in.next();
        }
    }
      
    while(true){
    System.out.print("Employment Status(regular,probationary,contractual,temporary): ");
    String text2=in.nextLine();
    if(text2.matches("[a-zA-Z ]+")){
    empstat=text2;
    break;
    }else{
    System.out.println("Invalid input. Try again.");
        }
    }
    
    while(true){
    System.out.print("Civil Status(single,married,widowed): ");
    String text3=in.nextLine();
    if(text3.matches("[a-zA-Z ]+")){
    civstat=text3;
    break;
    }else{
    System.out.println("Invalid input. Try again.");
        }
    }
    
    while(true){
    System.out.print("Dependents: ");
    if(in.hasNextInt()){
    dependent=in.nextInt();
    in.nextLine();
    break;
    }else{
    System.out.println("Invalid input. Try again.");
    in.next();
        }
    }

    while(true){
    System.out.print("Labor Union Member? (yes, otherwise no): ");
    String text4=in.nextLine();
    if(text4.matches("[a-zA-Z ]+")){
    labor=text4;
    break;
    }else{
    System.out.println("Invalid input. Try again.");
    in.next();
    }
    
    }
    
    while(true){
    System.out.print("In the Company loan program? (yes, otherwise no): ");
    String text5=in.nextLine();
    if(text5.matches("[a-zA-Z ]+")){
    company=text5;
    break;
    }else{
    System.out.println("Invalid input. Try again.");
    in.next();
        }
    }
    System.out.println("\nEmployee Added in the Record.") ;   
    valid=true;
    }
    
public void compute(){
    //Rate
    double rph=0, rpd=0;
    if(empstat.equalsIgnoreCase("regular")){
        rpd=800;
    }else if(empstat.equalsIgnoreCase("probationary")){
        rpd=600;
    }else if(empstat.equalsIgnoreCase("contractual")){
        rpd=500;
    }else if(empstat.equalsIgnoreCase("temporary")){
        rpd=450;
    }else{
        rpd=400;
    }
    
    rph=rpd/8.0;
    
    //HOUR COMPUTATION
    if(hours>120){
     overtime=hours-120.0;
     basicpay=120*rph;
     overpay=1.5*rph*overtime;
     gross=basicpay+overpay;
     }else{
     overtime=0;
     overpay=0;
     basicpay=hours*rph;
     gross=basicpay+overpay;
     }

    //SSS
    double sss=0, addsss=0, rate=0;
     if(gross<=5000){
         rate=0.05;
     }else if(gross<=10000){
         rate=0.08;
     }else if(gross<=20000){
         rate=0.10;
         if(empstat.equalsIgnoreCase("regular")){
             addsss=0.01;
         } 
     }else{
         rate=0.12;
         if(dependent>=3){
             addsss=0.02;
         }
     }
     
     sss=gross*(rate+addsss);

    //WTAX
    double wtax=0, tax=0, excess=0, prexcess=0, adjustment=0;
     if(gross<=8000){
         tax=0;
     }else if(gross<=20000){
         tax=500;
         excess=gross-8000;
         prexcess=0.10*excess;
         
         if(civstat.equalsIgnoreCase("married")){
             adjustment = -0.05*gross;
         }
     }else if(gross<=35000){
         tax=1700;
         excess=gross-20000;
         prexcess=0.15*excess;
     }else if(gross<=50000){
         tax=4000;
         excess=gross-35000;
         prexcess=0.20*excess;
         
         if(civstat.equalsIgnoreCase("single")){
             adjustment=0.05*gross;
         }
     }else{
         tax=7000;
         excess=gross-50000;
         prexcess=0.25*excess;
     }
    
     wtax=tax+prexcess+adjustment;
     
     //PHILHEALTH
    double philhealth=0, base1=0, adjust=0;
    if(civstat.equalsIgnoreCase("single")){
        base1=500;
        if(dependent==1){
              adjust=100;
            } else if(dependent==2){
              adjust=200;
            } else if(dependent>=3){
              adjust=300; 
            }  
    }else if(civstat.equalsIgnoreCase("married")){
        base1=400;
        if(dependent==1){
              adjust=100;
            }else if(dependent==2){
              adjust=200;
            }else if(dependent>=3){
              adjust=300;  
            }
    }else if(civstat.equalsIgnoreCase("widowed")){
        base1=350;
    }else{
        base1=300;
        if(dependent == 1){
              adjust=100;
            }else if(dependent == 2){
              adjust=200;
            }else if(dependent >= 3){
              adjust=300;  
            }
    }
   
    philhealth=base1+adjust;
    
    //PAG-IBIG
     double pagibig=0, rate2=0, adjustment2=0;
     if(gross<=1500){
         rate2=0.01*gross;
     }else if(gross<=10000){
         rate2=0.02*gross;
         if(empstat.equalsIgnoreCase("temporary")){
             adjustment2=50;
         }
     }else{
         rate2=0.03*gross;
         if(empstat.equalsIgnoreCase("regular")){
             adjustment2=100;
         }
     }
     
     pagibig=rate2+adjustment2;

    //SpecialDeductions
     double spdeduct=0, union=0, penalty=0, healthloan=0;
     if(labor.equalsIgnoreCase("yes")){
         union=150;
     }
     if(hours<120){
         penalty=(120-hours)*50;
     }
     if(company.equalsIgnoreCase("yes")){
         healthloan=0.02*gross;
     }
     
     spdeduct=union+penalty+healthloan;
     totalded=sss+wtax+philhealth+pagibig+spdeduct;
     netincome=gross-totalded;
    }
    
public void display(){
    System.out.println("\n========PAYROLL========");
    System.out.println("Employee Number: "+empnumber);
    System.out.println("Employee Name: "+empName);
    System.out.println("Hours Worked: "+hours);
    System.out.println("Employment Status: "+empstat);
    System.out.println("Civil Status: "+civstat);
    System.out.println("Dependent: "+dependent);
    System.out.println("Labor Member Union: "+labor);
    System.out.println("Company Loan Program: "+company);
    System.out.println("Basic Pay: "+basicpay);
    System.out.println("Overtime Pay: "+overpay);
    System.out.println("Gross Income: "+gross);
    System.out.println("Total Deductions: "+totalded);
    System.out.println("Net Income: "+netincome);
    System.out.println("=======================");
    }
}


