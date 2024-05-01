import 'package:email_password_login/screens/login_screen.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
/*Future<void> main() async {
 WidgetsFlutterBinding.ensureInitialized();
 await Firebase.initializeApp();
 runApp(MyApp());
}*/
void main() async {
 WidgetsFlutterBinding.ensureInitialized();
 await Firebase.initializeApp(
 options: FirebaseOptions(
 apiKey: "AIzaSyAQVWkGN0uGA0RtsrCjd5aFahNxk5tHI9s", // Your apiKey
 appId: "1:307784514935:android:e8a36c3599fa89c930b572", // Your appId
 messagingSenderId: "307784514935", // Your messagingSenderId
 projectId: "auth-flutter-4245e", // Your projectId
 ),
 );
 runApp(MyApp());
}
class MyApp extends StatelessWidget {
 // This widget is the root of your application.
 @override
 Widget build(BuildContext context) {
 return MaterialApp(
 title: 'Email And Password Login',
 theme: ThemeData(
 primarySwatch: Colors.red,
 ),
 debugShowCheckedModeBanner: false,
 home: LoginScreen(),
 );
 }
}
