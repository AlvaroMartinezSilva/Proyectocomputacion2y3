import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NavbarComponent } from './pagina-inicio/pagina-inicio.component';
import { UserComponent } from './usuarios/usuarios.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    UserComponent
  ],

  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }