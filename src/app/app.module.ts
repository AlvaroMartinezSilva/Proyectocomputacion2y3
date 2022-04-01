import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NavbarComponent } from './components/navbar/navbar.component';
import { FooterComponent } from './components/footer/footer.component';
import { AnalisisSentimientosComponent } from './components/analisis-sentimientos/analisis-sentimientos.component';

import { HttpClientModule } from '@angular/common/http';
import { WelcomeComponent } from './components/welcome/welcome.component';
import { DescriptionComponent } from './components/description/description.component';
import { FlaskApiService } from './services/flask-api.service';
import { FormsModule } from '@angular/forms';

@NgModule({

  declarations: [
    AppComponent,
    NavbarComponent,
    FooterComponent,
    AnalisisSentimientosComponent,
    WelcomeComponent,
    DescriptionComponent
  ],

  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    HttpClientModule,
    FormsModule
  ],

  providers: [FlaskApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
