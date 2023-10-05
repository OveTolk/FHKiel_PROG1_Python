<template>
  <v-app>
    <v-container>
      <v-row>
        <v-col cols="12" md="6">
          <v-card class="dashboard-card">
            <v-card-title class="headline">{{
              projectData["Initiative name"]
            }}</v-card-title>
            <v-card-text>
              <v-row>
                <v-col cols="6" >
                  <div class="data-label" >Initiative goals:</div>
                  <div class="data-value">
                    {{ projectData["Initiative goals"] }}
                  </div>
                </v-col>
                <v-col cols="6">
                  <div class="data-label">Project leader:</div>
                  <div class="data-value">
                    {{ projectData["Project leader"] }}
                  </div>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="6">
                  <div class="data-label">Sponsor:</div>
                  <div class="data-value">{{ projectData["Sponsor"] }}</div>
                </v-col>
                <v-col cols="6">
                  <div class="data-label">Status:</div>
                  <div class="data-value">{{ projectData["Status"] }}</div>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="6">
                  <div class="data-label">Expected benefits:</div>
                  <div class="data-value">
                    {{ projectData["Expected benefits"] }}
                  </div>
                </v-col>
                <v-col cols="6">
                  <div class="data-label">Required investments:</div>
                  <div class="data-value">
                    {{ projectData["Required investments"] }}
                  </div>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="6">
                  <div class="data-label">Risks:</div>
                  <div class="data-value">{{ projectData["Risks"] }}</div>
                </v-col>
                <v-col cols="6">
                  <div class="data-label">Dependencies:</div>
                  <div class="data-value">
                    {{ projectData["Dependencies"] }}
                  </div>
                </v-col>
              </v-row>
              <v-row>
                <v-timeline ref="timeline" align="start">
                  <v-timeline-item
                    v-for="(datapoint, index) in dynamicDataPoints"
                    :key="index"
                    :dot-color="datapoint.color"
                    size="small"
                  >
                    <template v-slot:opposite>
                      <div
                        :class="`pt-1 headline font-weight-bold`"
                        v-text="datapoint.date"
                      ></div>
                    </template>
                    <div>
                      <h2
                        :class="`mt-n1 headline font-weight-light mb-4 text-${datapoint.color}`"
                      >
                        {{ datapoint.event }}
                      </h2>
                      <div>
                        {{ datapoint.description }}
                      </div>
                    </div>
                  </v-timeline-item>
                </v-timeline>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      projectData: {},
      dynamicDataPoints: [],
    };
  },
  methods: {
  },
  mounted() {
    // WebSocket-Verbindung herstellen
    const ws = new WebSocket("ws://ts.ovetolk.eu:3007");

    // Event-Handler für eingehende Nachrichten
    ws.addEventListener("message", (event) => {
      const data = JSON.parse(event.data);
      // Aktualisiere die Projektinformationen mit den empfangenen Daten
      this.projectData = data;
      this.dynamicDataPoints = data.Datapoints;
      console.log(data.Datapoints);
    });
  },
};
</script>

<style scoped>
.dashboard-card {
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.headline {
  font-size: 24px;
  text-align: center;
  margin-bottom: 20px;
}

.data-label {
  font-weight: bold;
  margin-top: 10px;
}

.data-value {
  margin-bottom: 10px;
}
</style>
