# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


package VVCE.NB;
import java.io.FileReader;
import java.io.IOException;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
public class v {
	public static void main(String[] args)throws IOException,ParseException{
	JSONParser jsonpaser =  new JSONParser();
	FileReader reader=new FileReader(".\\JSON\\demo.json");
	Object obj=jsonpaser.parse(reader);
	JSONObject empjsonobj=(JSONObject)obj;
	String fname=(String)empjsonobj.get("Firstname");
	String lname=(String)empjsonobj.get("lastname");
	System.out.println("First name:"+fname);
	System.out.println("Last name:"+lname);
	System.out.println("Your name is:" +fname+ " "+ lname);
	}

}
