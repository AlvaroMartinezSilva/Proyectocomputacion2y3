import { Component, Input, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FlaskApiService } from '../../services/flask-api.service';

@Component({
  selector: 'app-analisis-sentimientos',
  templateUrl: './analisis-sentimientos.component.html',
  styleUrls: ['./analisis-sentimientos.component.scss'],
  providers: [FlaskApiService]
})


export class AnalisisSentimientosComponent implements OnInit {
  textareaContent: string = '';
  json: any = false;
  imagen: any;
  result: any;

  texto = '';

  constructor(private http: HttpClient, private flask_api: FlaskApiService) { }

  ngOnInit(): void {
    this.flask_api.getAll().subscribe((res) =>
    {
      console.log('Res ', res)
    });

  }

  analizarTexto(){



    this.flask_api.analizarSentimiento(this.texto).subscribe((res) =>
    {
      console.log('Res ', res);
      console.log('Res',res.analisis.carita);
      this.texto='Sentimiento: '+res.analisis.carita+'\nResultado: '+res.analisis.sentimiento+'\nTexto: '+res.analisis.texto;

    });
  }








}
