// 1. Калькулятор умеет выполнять операции сложения, вычитания, умножения и деления с двумя числами: a + b, a - b, a * b, a / b.
// Данные передаются в одну строку (смотри пример)! Решения, в которых каждое число и арифмитеческая операция передаются с новой строки считаются неверными.
// 2. Калькулятор умеет работать как с арабскими (1,2,3,4,5...), так и с римскими (I,II,III,IV,V...) числами.
// 3. Калькулятор должен принимать на вход числа от 1 до 10 включительно, не более. На выходе числа не ограничиваются по величине и могут быть любыми.
// 4. Калькулятор умеет работать только с целыми числами.
// 5. Калькулятор умеет работать только с арабскими или римскими цифрами одновременно, при вводе пользователем строки вроде 3 + II калькулятор должен выбросить исключение
// и прекратить свою работу.
// 6. При вводе римских чисел, ответ должен быть выведен римскими цифрами, соответственно, при вводе арабских - ответ ожидается арабскими.
// 7. При вводе пользователем неподходящих чисел приложение выбрасывает исключение и завершает свою работу.
// 8. При вводе пользователем строки, не соответствующей одной из вышеописанных арифметических операций, приложение выбрасывает исключение и завершает свою работу.
// 9. Результатом операции деления является целое число, остаток отбрасывается.
// 10. Результатом работы калькулятора с арабскими числами могут быть отрицательные числа и ноль.
// Результатом работы калькулятора с римскими числами могут быть только положительные числа, если результат работы меньше единицы, выбрасывается исключение

import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("Введите арифметическое выражение (пример: '1 + 2' или 'I + II'):");
        Scanner in = new Scanner(System.in);
        String arithmeticExpressionStr = in.nextLine();
        calc(arithmeticExpressionStr);

    }
    public static void calc(String arithmeticExpressionStr) throws Exception {
        String [] arithmeticExpressionArray = arithmeticExpressionStr.split(" ");
        if(arithmeticExpressionArray.length == 3) {
               try {
                   int a = Integer.parseInt(arithmeticExpressionArray[0]);
                   int b = Integer.parseInt(arithmeticExpressionArray[2]);
                   if(a > 0 && a < 11 && b > 0 && b < 11){
                       System.out.println(calcArabic(a,b,arithmeticExpressionArray[1]));
                   }
                   else {
                       System.out.println("Калькулятор должен принимать на вход числа от 1 до 10 включительно, не более");
                   }
               } catch (NumberFormatException e) {
                   try {
                       int a = Number.valueOf(arithmeticExpressionArray[0]).getArabic();
                       int b = Number.valueOf(arithmeticExpressionArray[2]).getArabic();
                       if(a > 0 && a < 11 && b > 0 && b < 11) {
                           int resultArabic = calcArabic(a, b, arithmeticExpressionArray[1]);
                           if (resultArabic > 0){
                               Number resultRoman = Number.values()[resultArabic - 1];
                               System.out.println(resultRoman);
                           }
                           else{
                               System.out.println("в римской системе нет чисел меньше 1");
                           }
                       }
                       else {
                           System.out.println("Калькулятор должен принимать на вход числа от 1 до 10 включительно, не более");
                       }
                   }
                   catch (IllegalArgumentException z){
                       System.out.println("формат математической операции не удовлетворяет заданию (используются одновременно разные системы счисления, либо не допустимые символы)");
                   }
               }
        } else {
            System.out.println("формат математической операции не удовлетворяет заданию - два операнда и один оператор через пробел");
            }
            }


    static int calcArabic(int a, int b, String operator){
        return switch (operator) {
            case "+" -> a+b;
            case "-" -> a-b;
            case "*" -> a*b;
            case "/" -> a/b;
            default -> throw new IllegalStateException("Недопустимое значение оператора: " + operator);
        };
        }
}
