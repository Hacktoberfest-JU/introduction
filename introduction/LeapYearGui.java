// A simple GUI Leap Year Calculator Made In JAVA LANGUAGE
// Name: Yashwant Soni      Class: Btech 1st Year       Sec: E
import javax.swing.JOptionPane;
public class LeapYearGui {
    public static void main(String[] args) {
        int year = Integer.parseInt(JOptionPane.showInputDialog("Enter Year: "));

        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0){
            JOptionPane.showMessageDialog(null, "It's a Leap Year");
        }
        else{
            JOptionPane.showMessageDialog(null, "It's not a Leap Year");
        }
    }
}
