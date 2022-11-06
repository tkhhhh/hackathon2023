import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.scss'],
  providers: [HttpClient]
})
export class WelcomeComponent implements OnInit {

  isSpinning = true;
  accountDetailsisSpinning = true;

  inputValue = "";
  typeValue = "";
  purpose = "";
  purpose_url = "";
  purpose_param = {};
  isVisible = false;

  recentTransactions: ItemData[] = [];
  accountDetails: AccountDetails = {firstname: "",lastname: "",homeAddress: "",email:"", phoneNumber:""};
  accountID = "73680920";

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.post<any>('/api/transaction/recently', { accountID: this.accountID, amount: 4, day: 360 }).subscribe(data => {
        for (let i=0; i<data["Transactions"].length; i++) {
          this.recentTransactions.push({
            amount:data["Transactions"][i].amount,
            merchant:data["Transactions"][i].merchant.name,
            timestamp:data["Transactions"][i].timestamp,
          })
        }
        this.isSpinning = false;
    });
    this.http.post<any>('/api/account/details', { accountID: this.accountID}).subscribe(data => {
      this.accountDetails = {
        firstname: data["firstname"],
        lastname: data["lastname"],
        homeAddress: data["homeAddress"],
        email: data["email"],
        phoneNumber: data["phoneNumber"]
      };
      console.log(data);
      this.accountDetailsisSpinning = false;
    });
  }

  getInput(): void {
    this.typeValue = ""
    let s = this.inputValue.substring(0, this.inputValue.length - 1)
    if(this.inputValue.indexOf('\n') !== this.inputValue.length - 1) {
      s = this.inputValue.substring(this.inputValue.lastIndexOf("\n", this.inputValue.length-2) + 1, this.inputValue.lastIndexOf("\n"))
    }
    this.http.post<any>('/api/robot', { accountID: this.accountID, purpose: s}).subscribe(data => {
        this.purpose = data.purpose
        this.purpose_url = data.purpose_url
        this.purpose_param = data.param
        this.isVisible = true
    })
  }

  typeChange(): void {
    this.inputValue += (this.typeValue + "\n")
    this.getInput()
  }

  handleOk(): void {
    this.http.post<any>(this.purpose_url, this.purpose_param).subscribe(data => {
      if(this.purpose === "report") //navigator
      this.handleCancel()
    })
  }

  handleCancel(): void {
    this.isVisible = false
    this.purpose = "";
    this.purpose_url = "";
  }

}

interface ItemData {
  timestamp: string;
  merchant: string;
  amount: number;
}
interface AccountDetails {
  firstname: string,
  lastname: string,
  homeAddress: string,
  email: string,
  phoneNumber: string
}
