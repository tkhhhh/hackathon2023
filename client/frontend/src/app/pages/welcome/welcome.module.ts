import { NgModule } from '@angular/core';

import { WelcomeRoutingModule } from './welcome-routing.module';

import { WelcomeComponent } from './welcome.component';
import {NzButtonModule} from "ng-zorro-antd/button";
import {NzGridModule} from "ng-zorro-antd/grid";
import {NzCardModule} from "ng-zorro-antd/card";
import {NzTableModule} from "ng-zorro-antd/table";
import {CommonModule} from "@angular/common";
import {NzSpinModule} from "ng-zorro-antd/spin";
import {NzInputModule} from "ng-zorro-antd/input";
import {FormsModule} from "@angular/forms";
import {NzModalModule} from "ng-zorro-antd/modal";


@NgModule({
  imports: [WelcomeRoutingModule, NzButtonModule, NzGridModule, NzCardModule, NzTableModule, CommonModule, NzSpinModule, NzInputModule, FormsModule, NzModalModule],
  declarations: [WelcomeComponent],
  exports: [WelcomeComponent]
})
export class WelcomeModule { }
