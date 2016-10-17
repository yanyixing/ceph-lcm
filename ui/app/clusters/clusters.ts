import { Component, ViewChild } from '@angular/core';
import { Modal, Filter } from '../directives';
import { DataService } from '../services/data';
import { Cluster } from '../models';

import * as _ from 'lodash';

@Component({
  templateUrl: './app/templates/clusters.html'
})
export class ClustersComponent {
  clusters: Cluster[] = null;
  newCluster: Cluster = new Cluster({});
  @ViewChild(Filter) filter: Filter;

  constructor(private data: DataService, private modal: Modal) {
    this.fetchData();
  }

  fetchData() {
    this.data.cluster().findAll({filter: _.get(this.filter, 'query', {})})
      .then(
        (clusters: Cluster[]) => this.clusters = clusters,
        (error: any) => this.data.handleResponseError(error)
      );
  }

  editCluster(cluster: Cluster = null) {
    this.newCluster = _.isNull(cluster) ? new Cluster({}) : cluster.clone();
    this.modal.show();
  }

  save() {
    var savePromise: Promise<any>;
    if (this.newCluster.id) {
      // Update cluster
      savePromise = this.data.cluster().postUpdate(this.newCluster.id, this.newCluster);
    } else {
      // Create new cluster
      savePromise = this.data.cluster().postCreate(this.newCluster);
    }
    return savePromise
      .then(
        () => {
          this.modal.close();
          this.fetchData();
        },
        (error: any) => this.data.handleResponseError(error)
      );
  }
}