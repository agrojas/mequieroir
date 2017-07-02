/**
 * Proposals DataService
 * Uses embedded, hard-coded data model; acts asynchronously to simulate
 * remote data service call(s).
 *
 * @returns {{loadAll: Function}}
 * @constructor
 */
function ProposalsDataService($http, $q) {
  
  var proposals = []
   
   function handleSuccess(data, status, headers, config) {
    // use data, status, headers, config
          data.data.data.proposals.forEach(prop => {
            proposals.push(prop.proposal)
          });

          return $q.when(proposals);
  }

  function handleError(data, status, headers, config) {
    // handle errors
      var promise = $q.reject();
      return promise;
  }

  // Promise-based API
  
  return {
    loadAllProposals: function(userId) {
      // Simulate async nature of real remote calls
        console.log('userId',userId);
        return $http({
          method: 'GET',
          url: 'http://localhost:8090/mqis/2/results/'
        }).then(handleSuccess,handleError);

    }
  };
}

export default ["$http", "$q", ProposalsDataService];

