package org.data.master.infrastructure.api.client;


import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.QueryParam;
import org.data.master.infrastructure.dto.CovidMovementDTO;
import org.eclipse.microprofile.rest.client.annotation.ClientHeaderParam;
import org.eclipse.microprofile.rest.client.inject.RegisterRestClient;

import java.util.List;

@RegisterRestClient(baseUri = "https://api.portaldatransparencia.gov.br/api-de-dados/coronavirus")
public interface RespiratoryDiseasesGovClient {


    @GET
    @Path("/movimento-liquido-despesa")
    @ClientHeaderParam(name = "chave-api-dados", value="3c4bcf7c1df7ef33fa632269bb9e34eb")
    List<CovidMovementDTO> getExtensionsById(
            @QueryParam("mesAnoLancamento") String yearMonth,
            @QueryParam("pagina") Integer page
    );
}
