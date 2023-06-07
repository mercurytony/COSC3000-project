package textures;

public class TerrainTexturePack {
	private TerrainTexture modelTexture;
	private TerrainTexture rTexture;
	private TerrainTexture gTexture;
	private TerrainTexture bTexture;
	
	public TerrainTexturePack(TerrainTexture modelTexture, TerrainTexture rTexture, TerrainTexture gTexture,
			TerrainTexture bTexture) {

		this.modelTexture = modelTexture;
		this.rTexture = rTexture;
		this.gTexture = gTexture;
		this.bTexture = bTexture;
	}

	public TerrainTexture getModelTexture() {
		return modelTexture;
	}

	public TerrainTexture getrTexture() {
		return rTexture;
	}

	public TerrainTexture getgTexture() {
		return gTexture;
	}

	public TerrainTexture getbTexture() {
		return bTexture;
	}

	
	
	
}
