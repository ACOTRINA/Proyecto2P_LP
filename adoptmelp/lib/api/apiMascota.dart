import 'dart:convert';
import '../modelos/mascota.dart';
import 'package:http/http.dart' as http;

class MascotaProvider{

  final url="http://10.0.2.2:8000/api/mascotas";

  Future<List<Mascota>> getMascotasAdopcion() async {

    List<Mascota> mascotas = [];
    final response = await http.get(url);
    if(response.statusCode==200){
      var datos=json.decode(response.body) as List;
      mascotas = datos.map<Mascota>((json) => Mascota.fromJson(json)).toList();
      return mascotas;
    }
    return mascotas;
  }


}