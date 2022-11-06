import { Component, OnInit } from '@angular/core';
import { EChartsOption } from 'echarts';
import {HttpClient} from "@angular/common/http";
import {NzNotificationService} from "ng-zorro-antd/notification";

@Component({
  selector: 'app-budget',
  templateUrl: './budget.component.html',
  styleUrls: ['./budget.component.scss'],
  providers: [NzNotificationService]
})
export class BudgetComponent implements OnInit {

  option : EChartsOption = {};
  accountID = "73680920";
  isLoading = true;
  constructor(private http: HttpClient, private notification: NzNotificationService) { }

  ngOnInit(): void {
    this.http.post<any>('/api/pie/chart', { accountID: this.accountID}).subscribe(data => {
        this.option = {
        title: {
          text: 'Transaction pie chart',
          subtext: 'from capitalOne',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: Object.keys(data).map((x: string | number) => {
              return { value: Math.abs(data[x]), name: x};
            }),
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };
        this.isLoading = false;
    })
  }

  createBasicNotification(): void {
    this.notification
      .blank(
        'Result',
        'The report has sent to your email.'
      )
      .onClick.subscribe(() => {
      });
  }

  download(): void {
    this.http.post("/api/ss", {accountID: this.accountID}).subscribe(data => {
          this.createBasicNotification()
        })
  }

}
