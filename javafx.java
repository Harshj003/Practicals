// Login Form using Javafx
import javafx.application.Application;
import javafx.beans.Observable;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;
import java.io.IOException;
public class HelloApplication extends Application
{
@Override
public void start(Stage stage) throws IOException
{
Label nameLabel=new Label("Name");
TextField nameText=new TextField();
Label dobLabel=new Label("Date of birth");
DatePicker datePicker=new DatePicker();
Label genderLabel=new Label("Gender");
ToggleGroup groupGender=new ToggleGroup();
RadioButton maleRadio=new RadioButton("male");
maleRadio.setToggleGroup(groupGender);
RadioButton femaleRadio=new
RadioButton("female");
femaleRadio.setToggleGroup(groupGender);
Label technologiesLabel=new Label("What technologies do you know?");
CheckBox javaCheckBox=new CheckBox("Java");
javaCheckBox.setIndeterminate(false);
CheckBox dotnetCheckBox=new CheckBox("Python");
javaCheckBox.setIndeterminate(false);
dotnetCheckBox = new CheckBox("R");
javaCheckBox.setIndeterminate(false);
Label educationLabel=new Label("Educational qualification");
ListView eduList=new ListView();
ObservableList data= FXCollections.observableArrayList();
data.addAll("Std 12","Bachelor","Master","Phd.");
eduList.setItems(data);
eduList.setPrefSize(100,100);
Label locationLabel=new Label("Location");
ChoiceBox locationChoiceBox=new ChoiceBox();
locationChoiceBox.getItems().addAll(
"Kolkata","Delhi","Chennai","Mumbai","Bengaluru","Pune",
"Ahmedabad","Chandigarh","Jaipur","Thiruvananthapuram",
"Hyderabad","Gandhinagar","Ranchi","Gangtok","Shillong",
"Patna","Out of India");
Button buttonRegister=new Button("Register");
GridPane gridPane=new GridPane();
gridPane.setMinSize(500,300);
gridPane.setPadding(new Insets(10,10,10,10));
gridPane.setVgap(5);
gridPane.setHgap(5);
gridPane.setAlignment(Pos.CENTER);
gridPane.add(nameLabel,0,0);
gridPane.add(nameText,1,0);
gridPane.add(dobLabel,0,1);
gridPane.add(datePicker,1,1);
gridPane.add(genderLabel,0,2);
gridPane.add(maleRadio,1,2);
gridPane.add(femaleRadio,2,2);
gridPane.add(technologiesLabel,0,3);
gridPane.add(javaCheckBox,1,3);
gridPane.add(dotnetCheckBox,2,3);
gridPane.add(educationLabel,0,4);
gridPane.add(eduList,1,4);
gridPane.add(locationLabel,0,5);
gridPane.add(locationChoiceBox,1,5);
gridPane.add(buttonRegister,2,7);
buttonRegister.setStyle("-fx-background-color:darkslateblue; -fx-text-fill: white;");
nameLabel.setStyle("-fx-font:normal bold 15px 'serif' ");
dobLabel.setStyle("-fx-font:normal bold 15px 'serif' ");
genderLabel.setStyle("-fx-font:normal bold 15px 'serif' ");
technologiesLabel.setStyle("-fx-font:normal bold 15px 'serif' ");
educationLabel.setStyle("-fx-font:normal bold 15px 'serif' ");
locationLabel.setStyle("-fx-font:normal bold 15px 'serif' ");
gridPane.setStyle("-fx-background-color:LightBlue;");
Scene scene=new Scene(gridPane);
stage.setTitle("Registration Form"); 
stage.setScene(scene);
stage.show();
}
public static void main(String[] args)
{
launch();
}
}
