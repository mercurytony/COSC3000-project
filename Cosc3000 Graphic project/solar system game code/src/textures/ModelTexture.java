package textures;

public class ModelTexture {
	
	private int textureID;
	private int specularMap;
	private boolean hasTransparency = false;
	private boolean useFakeLighting = false;
	private boolean hasSpecularMap = false;
	
	private float shineDamper = 1;
	private float reflectivity = 0;
	
	private int numberOfRows = 1;
	
	public void setSpecularMap(int specMap) {
		this.specularMap = specMap;
		this.hasSpecularMap = true;
	}
	
	public boolean hasSpecularMap() {
		return hasSpecularMap;
	}
	
	public int getSpecularMap() {
		return specularMap;
	}
	
	
	
	public void setNumberOfRows(int numberOfRows) {
		this.numberOfRows = numberOfRows;
	}

	public ModelTexture(int texture){
		this.textureID = texture;
	}
	
	public boolean isUseFakeLighting() {
		return useFakeLighting;
	}

	public void setUseFakeLighting(boolean useFakeLighting) {
		this.useFakeLighting = useFakeLighting;
	}

	public boolean isHasTransparency() {
		return hasTransparency;
	}



	public void setHasTransparency(boolean hasTransparency) {
		this.hasTransparency = hasTransparency;
	}



	public int getID(){
		return textureID;
	}

	public float getShineDamper() {
		return shineDamper;
	}

	public void setShineDamper(float shineDamper) {
		this.shineDamper = shineDamper;
	}

	public float getReflectivity() {
		return reflectivity;
	}

	public void setReflectivity(float reflectivity) {
		this.reflectivity = reflectivity;
	}

	public int getNumberOfRows() {
		// TODO Auto-generated method stub
		return numberOfRows;
	}
	
	

}