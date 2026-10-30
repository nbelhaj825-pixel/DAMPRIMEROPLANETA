import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        double maximo=-1,minimo=11,nota;
        int cmaximo=0,cminimo=0;


        for(int i=1;i<=5;i++){

            System.out.print("Dime la nota");
            nota=sc.nextDouble();

            if (nota>maximo) {
                maximo = nota;
                cmaximo = 1;
            } else if (nota==maximo) {
                cmaximo += 1;
            }

            if (nota<minimo) {
                minimo = nota;
                cminimo = 1;
            } else if (nota==minimo) {
                cminimo += 1;
            }


        }
        System.out.printf("maximo :%.2f cmaximo :%d\n" ,maximo,cmaximo);
        System.out.printf("minimo :%.2f cminimo :%d\n" ,minimo,cminimo);


    }


}