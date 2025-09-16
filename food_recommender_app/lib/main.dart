import 'package:flutter/material.dart';
import 'upload_food_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Food Recommender App',
      theme: ThemeData(
        primarySwatch: Colors.orange,
      ),
      home: UploadFoodScreen(),
    );
  }
}
