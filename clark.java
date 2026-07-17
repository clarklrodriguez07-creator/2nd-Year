import java.util.*;
class clark{
    public static Scanner in=new Scanner(System.in);
    public static void main(String args[]){
        int n=in.nextInt();
        int a[]=new int[n];
        for(int i=0;i<n;i++){
            a[i]=in.nextInt();
        }
        Arrays.sort(a);
        for(int i=0;i<n;i++){
            System.out.print(a[i]+" ");
        }
    }

}